import React from "react";

const DocPage = ({ Content }) => {
    return (
        <div className="flex flex-col min-h-screen">
            <main className="prose">
                <Content />
            </main>
        </div>
    );
};

export default DocPage;
