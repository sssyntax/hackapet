import React from 'react';
import { MDXProvider } from '@mdx-js/react';

const DocPage = ({ Content }) => {
  return (
    <MDXProvider>
      <div className="flex flex-col min-h-screen">
        <Content />
      </div>
    </MDXProvider>
  );
};

export default DocPage;