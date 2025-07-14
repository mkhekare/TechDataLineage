import React from 'react';
import FileUpload from '../components/FileUpload';
import RepositoryLinkInput from '../components/RepositoryLinkInput';
import LineageGraph from '../components/LineageGraph';

const HomePage = () => {
    return (
        <div>
            <h1>AI-Powered Data Lineage Generator</h1>
            <FileUpload />
            <RepositoryLinkInput />
            <LineageGraph />
        </div>
    );
};

export default HomePage;