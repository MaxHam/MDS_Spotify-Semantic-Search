import { useState } from 'react';

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
        console.log(searchTerm);
    }
    return (
        <>
            <form onSubmit={handleSubmit}>
                <label>
                    Search for a track:
                    <input type="text" value={searchTerm} onChange={handleChange} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </>
    );
};

export default Search;