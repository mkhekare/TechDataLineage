import React, { useEffect, useRef } from 'react';
import mermaid from 'mermaid'; // Still import to use mermaid.run()

const LineageGraph = ({ graphDefinition }) => {
    const mermaidContainerRef = useRef(null);

    useEffect(() => {
        if (graphDefinition && mermaidContainerRef.current) {
            // Set the innerHTML directly
            mermaidContainerRef.current.innerHTML = graphDefinition;
            
            // Tell mermaid to process the content within this specific element
            try {
                mermaid.run({
                    nodes: [mermaidContainerRef.current]
                });
            } catch (e) {
                console.error("Mermaid rendering error:", e);
                mermaidContainerRef.current.innerHTML = `<pre>Error rendering graph: ${e.message}</pre>`;
            }
        }
    }, [graphDefinition]);

    return (
        <div className="lineage-graph">
            <div ref={mermaidContainerRef} className="mermaid">
                {/* Initial content or fallback for non-JS environments */}
                {/* This will be replaced by mermaid.run() */}
                {graphDefinition}
            </div>
        </div>
    );
};

export default LineageGraph;