#include <string>
#include <list>
#include <iostream>
#include <C:\Users\elgue\documents\DataStructures\Playlist\playlist_interface.h>
#include <windows.h>
using namespace std;

struct song 
{
    string data;
    song *next;
    song *prev;
};


class playlist : public IPlaylist
{
    private:
        song *head, *tail;
    public:
        song *playing;
        playlist()
        {
          head=NULL;
          tail=NULL;
          playing=NULL;
        }
        
    void add_song(string value)
    {
      song *temp=new song;
      temp->data=value;
      temp->next=NULL;

      if(head==NULL)
      {
        head=temp;
        tail=temp;
        temp=NULL;
      }
      else
      {	
        tail->next=temp;
        tail->next->prev = tail;
        tail=temp;
      }
    }
    
    void delete_song(int pos)
    {
        song *current=new song;
        song *previous=new song;
        current=head;
        for(int i=1;i<pos;i++)
        {
            previous=current;
            current=current->next;
            
        }
        previous->next=current->next;
        previous->next->prev = previous;
    }

    list<string> display()
    {
        list<string> list;
        song *temp=new song;
        temp=head;
        while(temp!=NULL)
        {
            list.push_back(temp->data);
            temp=temp->next;
        }
        return list;
    } 

    void play_now(string song_to_play)
    {
        song *temp=new song;
        temp = head;
        while(temp!=NULL)
        {
            if(temp->data == song_to_play)
            {
                playing=temp;
            }
            temp=temp->next;
        }
    }
    
    void play_next()
    {
        playing = playing->next;
    }
    
    void play_previous()
    {
        playing = playing->prev;
    }

    void destroy()
    {
        delete this;
    }
    
};


// extern "C" __declspec(dllexport) IPlaylist* __cdecl create_playlist()
// {
//     return new playlist;
// }



void showlist(list<string> g) 
{ 
    list <string> :: iterator it; 
    for(it = g.begin(); it != g.end(); ++it) 
        cout << '\t' << *it; 
    cout << '\n'; 
} 





int main()
{
  playlist MyPlaylist;
  MyPlaylist.add_song("hola broqui");
  MyPlaylist.add_song("que pecs men");
  MyPlaylist.add_song("orale mijo");
  list<string> list1 = MyPlaylist.display();
  showlist(list1);
  MyPlaylist.delete_song(2);
  list<string> list2 = MyPlaylist.display();
  showlist(list2);
  MyPlaylist.add_song("kkk");
  MyPlaylist.add_song("qqq");
  MyPlaylist.add_song("lll");
  list<string> list3 = MyPlaylist.display();
  showlist(list3);
  MyPlaylist.play_now("orale mijo");
  cout<<MyPlaylist.playing->data<<'\t';
  MyPlaylist.play_next();
  MyPlaylist.play_next();
  MyPlaylist.play_previous();
  MyPlaylist.play_previous();
  MyPlaylist.play_previous();

  cout<<MyPlaylist.playing->data<<'\t';

}