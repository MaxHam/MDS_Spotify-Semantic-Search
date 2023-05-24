/* eslint-disable @typescript-eslint/ban-ts-comment */
import { useEffect, useMemo, useState } from 'react';
import { ITrack } from '../../interfaces/Track';
import './AudioPlayer.css';
// @ts-ignore
import SpotifyPlayer from 'react-spotify-web-playback';

interface AudioPlayerProps {
    track: ITrack;
    token: string;
}


const AudioPlayer: React.FC<AudioPlayerProps> = (props) => {

    const { track, token } = props;
    const trackUri = useMemo( () => track.track_id ? [`spotify:track:${track.track_id}`] : null, [track.track_id]);
    const [play, setPlay] = useState(false);

    const handleCallback = (state: any) => {
        if (!state.isPlaying) {
            setPlay(false);
        }
    }


    useEffect(() => {
      setPlay(true);
    }, [trackUri]);
  
    if (!token) return null;
    return (
      <div className='audio-player'>
        <SpotifyPlayer
        token={token}
        hideAttribution
        callback={handleCallback}
        play={play}
        uris={trackUri ? trackUri : []}
        styles={{
          activeColor: '#fff',
          bgColor: '#333',
          color: '#fff',
          loaderColor: '#fff',
          sliderColor: '#1cb954',
          trackArtistColor: '#ccc',
          trackNameColor: '#fff',
          height: '55px',
        }}
      />
      </div>
    );
  };

export default AudioPlayer;
