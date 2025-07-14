import React, { useEffect } from 'react';
import mermaid from 'mermaid';

const LineageGraph = ({ graphDefinition }) => {
    useEffect(() => {
        if (graphDefinition) {
            // Initialize mermaid once (or ensure it's initialized)
            mermaid.initialize({ startOnLoad: false }); // We will manually run it
            
            // Render the graph. mermaid.run() processes all elements with class 'mermaid'
            // This ensures it re-renders when graphDefinition changes
            try {
                mermaid.run({
                    nodes: document.querySelectorAll('.mermaid')
                });
            } catch (e) {
                console.error("Mermaid rendering error:", e);
            }
        }
    }, [graphDefinition]);

    return (
        <div className="lineage-graph">
            <div className="mermaid">
                {graphDefinition}
            </div>
        </div>
    );
};

export default LineageGraph;