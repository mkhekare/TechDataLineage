import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import mermaid from 'mermaid';

mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose',
  fontFamily: 'Roboto, sans-serif',
  fontSize: '16px', // Increased font size for better readability
});

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);