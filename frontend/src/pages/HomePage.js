import React, { useState } from 'react';
import FileUpload from '../components/FileUpload';
import RepositoryLinkInput from '../components/RepositoryLinkInput';
import LineageGraph from '../components/LineageGraph';

const HomePage = () => {
    const [lineageGraph, setLineageGraph] = useState('graph TD;
    A[No Data Processed Yet]');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    const handleProcess = async (data, type) => {
        const formData = new FormData();
        if (type === 'file') {
            formData.append('file', data);
        } else if (type === 'repo') {
            formData.append('repo_link', data);
        }

        try {
            const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();

            if (response.ok) {
                setMessage(result.message);
                setLineageGraph(result.lineage);
                setError('');
            } else {
                setError(result.error || 'An unknown error occurred');
                setMessage('');
                setLineageGraph('');
            }
        } catch (err) {
            setError('Network error or server is unreachable.');
            setMessage('');
            setLineageGraph('');
        }
    };

    return (
        <div>
            <h1>AI-Powered Data Lineage Generator</h1>
            <FileUpload onFileUpload={(file) => handleProcess(file, 'file')} />
            <RepositoryLinkInput onRepoSubmit={(link) => handleProcess(link, 'repo')} />
            {message && <p style={{ color: 'green' }}>{message}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <LineageGraph graphDefinition={lineageGraph} />
        </div>
    );
};

export default HomePage;