import { useEffect, useState } from 'react';
import { ITrack } from '../../interfaces/Track';
import Track from '../Track/Track';
import './TrackInfo.css';
import { getNearText } from '../../api/weaviate';

interface TrackInfoProps {
    track: ITrack;
    token: string;
    onSelect: (track: ITrack) => void;
}

const TrackInfo: React.FC<TrackInfoProps> = (props) => {
    const { track, token, onSelect } = props;

    const { track_name, artist_name, album_name, lyrics  } = track;

    const [similarTracks, setSimilarTracks] = useState<ITrack[]>([]);

    useEffect(() => {
        getNearText([track_name, artist_name, album_name, lyrics], 3).then((newTracks) => setSimilarTracks(newTracks));
      }, [track_name, artist_name, album_name, lyrics])

    return (
        <div className='track-info'>
            <h2><b>{track.track_name}</b></h2>
            <h3>{track.artist_name}</h3>
            <h3>{track.album_name}</h3>

            <div className='similar-tracks'>
                <h2>Similar Songs</h2>
                <div className='similar-tracks-container'>
                    {similarTracks.map((track, index) => {
                        return <Track token={token} key={index} track={track} selected={track.track_id === track?.track_id} onSelect={onSelect} />
                    })}
                </div>
            </div>
            <div className='lyrics'>
                <h2>Lyrics</h2>
                <p>{track.lyrics}</p>
            </div>
            
        </div>
    );
}

export default TrackInfo;