import { useState } from 'react';
import { ITrack } from '../../interfaces/Track';
import './AudioPlayer.css';

interface AudioPlayerProps {
    track: ITrack;
    token: string;
}

const AudioPlayer: React.FC<AudioPlayerProps> = (props) => {
    const { track, token } = props;
    const [audio, setAudio] = useState<HTMLAudioElement | null>(null);
    const [isPlaying, setIsPlaying] = useState<boolean>(false);
    const [progress, setProgress] = useState<number>(0);
    const [duration, setDuration] = useState<number>(0);
    const [currentTime, setCurrentTime] = useState<number>(0);

    return (
        <div>
            <div className="audio-player">
                <div className="track-info">
                    <h2><b>{track.track_name}</b></h2>
                    <h3>{track.artist_name}</h3>
                    <h3>{track.album_name}</h3>
                </div>
                <div className="controls">
                    <div className="progress">
                        <p>{currentTime}</p>
                        <input type="range" value={progress} onChange={(e) => setProgress(parseInt(e.target.value))} />
                        <p>{Math.floor(track.duration_ms/1000)}s</p>
                    </div>
                    <div className="buttons">
                        <button onClick={() => setIsPlaying(!isPlaying)}>{isPlaying ? "Pause" : "Play"}</button>
                    </div>
                </div>
            </div>
            <div className='lyrics'>
                <h2>Lyrics</h2>
                <p>{track.lyrics}</p>
            </div>
        </div>
    );
};

export default AudioPlayer;
