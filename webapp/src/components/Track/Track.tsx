import { useCallback, useEffect, useState } from 'react';
import { getAlbum } from '../../api/spotify';
import { ITrack } from '../../interfaces/Track';
import './Track.css';

interface TrackProps extends ITrack {
    token: string;
}

const Track: React.FC<TrackProps> = (props) => {
    const { track_name, artist_name, album_name, album_id, token } = props;
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


    return (
        <div className='track'>
            <img className='album-art' src={albumArt} alt={album_name} />

            <div className='track_info-container'>
                <span className='track_info-text'>
                <b>{track_name}</b> - {artist_name} - {album_name}
                </span>
            </div>

        </div>
    );
};

export default Track;