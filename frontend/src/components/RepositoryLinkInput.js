import React, { useState } from 'react';

const RepositoryLinkInput = ({ onRepoSubmit }) => {
    const [repoLink, setRepoLink] = useState('');

    const handleChange = (event) => {
        setRepoLink(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (repoLink) {
            onRepoSubmit(repoLink);
            setRepoLink('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={repoLink}
                onChange={handleChange}
                placeholder="Enter Git repository link"
                required
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default RepositoryLinkInput;