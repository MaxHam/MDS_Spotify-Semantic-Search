import { useEffect, useState } from 'react'
import './Overview.css'
import { getAllTracks, getNearText } from '../../api/weaviate'
import Track from '../../components/Track/Track';
import { ITrack } from '../../interfaces/Track';
import Search from '../../components/Search/Search';

interface OverviewProps {
  token: string
}

function Overview(props:OverviewProps) {
  const { token } = props;
  const [tracks, setTracks] = useState<ITrack[]>([])

  useEffect(() => {
    getAllTracks().then((newTracks) => setTracks(newTracks));
  }, [])
  const handleChange = async(value: string) => {

    if(value === "" || !value) {
      return;
    }
    const newTracks = await getNearText([value]);
    setTracks(newTracks);
  }

  return (
    <>
      <h1>Spotify Semantic Search</h1>
      <Search onChange={handleChange} />
      <div className="grid-container">
          {tracks.map((track) => (
            <div className="grid-item">
             <Track key={track.track_id} token={token} {...track} />
            </div>
          ))}
      </div>
    </>
  )
}

export default Overview;