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
    const { track: selectedTrack, token, onSelect } = props;

    const { track_name, artist_name, album_name, lyrics  } = selectedTrack;

    const [similarTracks, setSimilarTracks] = useState<ITrack[]>([]);

    useEffect(() => {
        getNearText([track_name, artist_name, album_name, lyrics], 3).then((newTracks) => setSimilarTracks(newTracks));
      }, [track_name, artist_name, album_name, lyrics])

    return (
        <div className='track-info'>
            <h2><b>Title: </b>{selectedTrack.track_name}</h2>
            <h3><b>Artist: </b>{selectedTrack.artist_name}</h3>
            <h3><b>Album: </b>{selectedTrack.album_name}</h3>

            <h3><b>Genre: </b>{selectedTrack.genre.toUpperCase()}</h3>
            <h3><b>Subgenre: </b>{selectedTrack.subgenre}</h3>

            <div className='similar-tracks'>
                <h2>Similar Songs</h2>
                <div className='similar-tracks-container'>
                    {similarTracks.map((track, index) => {
                        return <Track token={token} key={index} track={track} selected={selectedTrack.track_id === track?.track_id} onSelect={onSelect} />
                    })}
                </div>
            </div>
            <div className='lyrics'>
                <h2>Lyrics</h2>
                <p>{selectedTrack.lyrics}</p>
            </div>
            
        </div>
    );
}

export default TrackInfo;