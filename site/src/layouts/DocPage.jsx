import React from 'react';

const DocPage = ({ Content }) => {
  return (
    <div className="flex flex-col min-h-screen">
      <Content />
    </div>
  );
};

export default DocPage;