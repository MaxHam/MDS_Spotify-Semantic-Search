interface ITrack {
    track_id: string;
    track_name: string;
    artist_name: string;
    album_name: string;
    album_id: string;
    duration_ms: number;
    lyrics: string;
    genre: string;
    subgenre: string;
  }

export type { ITrack }