import React, { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';

const LineageGraph = ({ graphDefinition }) => {
    const [svgContent, setSvgContent] = useState('');
    const [error, setError] = useState('');
    const uniqueId = useRef(`mermaid-graph-${Math.random().toString(36).substr(2, 9)}`);

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

    return (
        <div className="lineage-graph">
            {error && <pre style={{ color: 'red' }}>{error}</pre>}
            {svgContent ? (
                <div dangerouslySetInnerHTML={{ __html: svgContent }} />
            ) : (
                // Fallback for when graphDefinition is empty or rendering is in progress
                <pre>{graphDefinition}</pre>
            )}
        </div>
    );
};

export default LineageGraph;