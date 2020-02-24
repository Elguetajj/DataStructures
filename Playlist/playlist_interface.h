#include <string>
#include <list>
using namespace std;


class IPlaylist
{
    virtual void add_song(string value) = 0;
    virtual void delete_song(int pos) = 0;
    virtual list<string> display() = 0;
    virtual void play_now(string song_to_play) = 0;
    virtual void play_next() = 0;
    virtual void play_previous() = 0;
    virtual void destroy() = 0;
}