import { useState } from 'react';
import './QuestionSearch.css';

interface ISearch {
    value?: string;
    onChange: (text: string) => void;
}

const Search: React.FC<ISearch> = (props) => {
    const { value, onChange } = props;
    const [searchTerm, setSearchTerm] = useState<string>(value || "")
    const handleChange = async(event: any) => {
        setSearchTerm(event.target.value);
    }
    const handleSubmit = async(event: any) => {
        event.preventDefault();
        if(searchTerm=== "" || !searchTerm) {
            return;
        }
        onChange(searchTerm);
    }
    return (
        <>
            <form className='question-search-form' onSubmit={handleSubmit}>
                <label className='question-search-label'>
                    <input className='question-search-input' placeholder='What is love?' type="text" value={searchTerm} onChange={handleChange} />
                </label>
                <input className='submit-input' type="submit" value="Submit" />
            </form>
        </>
    );
};

export default Search;