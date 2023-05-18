import { useEffect, useState } from 'react'
import './Overview.css'
import { getAllTracks, getNearText } from '../../api/weaviate'
import Track from '../../components/Track/Track';
import { ITrack } from '../../interfaces/Track';
import Search from '../../components/Search/Search';
import QuestionSearch from '../../components/QuestionSearch/QuestionSearch';

interface OverviewProps {
  token: string
}

function Overview(props:OverviewProps) {
  const { token } = props;
  const [tracks, setTracks] = useState<ITrack[]>([])
  // False := Search, True := QuestionSearch
  const [mode, setMode] = useState<boolean>(false)

  const handleModeSwitch = () => {
    setMode(!mode);
  }

  useEffect(() => {
    getAllTracks().then((newTracks) => setTracks(newTracks));
  }, [])
  const handleChange = async(value: string) => {

    if(value === "" || !value) {
      return;
    }
    try {
      const newTracks = await getNearText([value]);
      if (newTracks.length === 0 || !newTracks) {
        return;
      }
      setTracks(newTracks);
    }
    catch(error) {
      console.log(error);
    }

  }

  return (
    <>
    <div className="header">
        <h1>Spotify Semantic Search</h1>
        <div className='mode-switch'>
        <span className="mode">Semantic</span>
        <label className="switch">
          <input type="checkbox" onChange={handleModeSwitch} checked={mode}/>
          <span className="slider round"></span>
        </label>
        <span className="mode">Question</span>
        </div>  
      </div>
      {!mode ? <div>
        <h3>Query tracks by their semantic lyric similarity to the search term</h3>
        <Search onChange={handleChange} />
        </div> :   <div>
        <h3>Ask questions about songs</h3>
        <QuestionSearch onChange={handleChange} />
          </div>}
    
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