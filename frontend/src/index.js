import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import mermaid from 'mermaid';

mermaid.initialize({
  startOnLoad: false, // We will manually trigger rendering
  theme: 'default', // You can change this to 'dark', 'forest', 'neutral'
  securityLevel: 'loose', // Allows more flexibility, but be aware of XSS risks with untrusted input
});

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);