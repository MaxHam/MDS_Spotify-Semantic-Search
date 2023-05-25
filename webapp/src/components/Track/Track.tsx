import { useEffect, useState } from 'react';
import { getAlbum } from '../../api/spotify';
import { ITrack } from '../../interfaces/Track';
import './Track.css';

interface TrackProps {
    track: ITrack;
    token: string;
    onSelect: (track: ITrack) => void;
    selected?: boolean;
}

const Track: React.FC<TrackProps> = (props) => {
    const { token, onSelect, track, selected } = props;
    const { track_name, artist_name, album_name, album_id } = track;
    const [albumArt, setAlbumArt] = useState<string>('');

    useEffect(() => {
        const getAlbumArt = async() => {
            try {
                const album = await getAlbum(album_id, token);
                setAlbumArt(album.images[0].url);
            }
            catch(error) {
                console.log(error);
            }
        };

        getAlbumArt()
    }, [album_id,token]);

    const handleClick = () => { 
        onSelect(track);
    }


    return (
        <button onClick={handleClick} className={`track ${selected ? 'selected' : ''}`}>
            <img className='album-art' src={albumArt} alt={album_name} />

            <div className='track_info-container'>
                <span className='track_info-text'>
                <b>{track_name}</b> - {artist_name} - {album_name}
                </span>
            </div>

        </button>
    );
};

export default Track;