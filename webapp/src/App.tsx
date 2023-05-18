import { useEffect, useState } from 'react';
import './App.css';
import Login from './pages/Login/Login';
import Overview from './pages/Overview/Overview';
import { getToken } from './api/spotify';

function App() {
  
  const [token, setToken] = useState('');

  const retrieveToken = async() => {
    try {
      const token = await getToken()
      setToken(token);
    }
    catch(error) {
      console.log(error);
    }
  }

  useEffect(() => {
    retrieveToken();
  }, []);

  return (
    <>
        { (token === '') ? <Login/> : <Overview token={token} /> }
    </>
  );
}

export default App
