import React, { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';
import domtoimage from 'dom-to-image';

const LineageGraph = ({ graphDefinition }) => {
    const [svgContent, setSvgContent] = useState('');
    const [error, setError] = useState('');
    const uniqueId = useRef(`mermaid-graph-${Math.random().toString(36).substr(2, 9)}`);
    const graphContainerRef = useRef(null); // Ref for the div containing the SVG

    useEffect(() => {
        if (graphDefinition) {
            setError(''); // Clear previous errors
            mermaid.render(uniqueId.current, graphDefinition)
                .then(({ svg }) => {
                    setSvgContent(svg);
                })
                .catch((e) => {
                    console.error("Mermaid rendering error:", e);
                    setError(`Error rendering graph: ${e.message}`);
                    setSvgContent(''); // Clear SVG content on error
                });
        } else {
            setSvgContent('');
            setError('');
        }
    }, [graphDefinition]);

    const handleDownloadImage = () => {
        if (graphContainerRef.current && svgContent) {
            domtoimage.toPng(graphContainerRef.current)
                .then(function (dataUrl) {
                    var link = document.createElement('a');
                    link.download = 'lineage-graph.png';
                    link.href = dataUrl;
                    link.click();
                })
                .catch(function (error) {
                    console.error('oops, something went wrong!', error);
                    setError('Failed to download image.');
                });
        }
    };

    return (
        <div className="lineage-graph">
            {error && <pre style={{ color: 'red' }}>{error}</pre>}
            {svgContent ? (
                <>
                    <button onClick={handleDownloadImage} style={{ marginBottom: '10px' }}>Download Graph as PNG</button>
                    <div ref={graphContainerRef} dangerouslySetInnerHTML={{ __html: svgContent }} />
                </>
            ) : (
                // Fallback for when graphDefinition is empty or rendering is in progress
                <pre>{graphDefinition}</pre>
            )}
        </div>
    );
};

export default LineageGraph;