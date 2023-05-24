import { useState } from 'react';
import './Search.css';

interface ISearch {
    value?: string;
    onChange: (text: string) => void;
}

const Search: React.FC<ISearch> = (props) => {
    const { value, onChange } = props;
    const [searchTerm, setSearchTerm] = useState<string>(value || "")
    const handleChange = async(event: any) => {
        setSearchTerm(event.target.value);
        onChange(searchTerm);
    }

    return (
        <>
            <form>
                <label>
                    <input className='search-input' placeholder=' Search for a track' type="text" value={searchTerm} onChange={handleChange} />
                </label>
            </form>
        </>
    );
};

export default Search;