import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import CodeGuide from "./pages/CodeGuide.mdx";
import Submitting from "./pages/Submitting.mdx";
import Faq from "./pages/Faq.mdx";

import DocPage from "./layouts/DocPage.jsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
    },
    {
        path: "/guide",
        element: <DocPage Content={CodeGuide} />,
    },
    {
        path: "/submitting",
        element: <DocPage Content={Submitting} />,
    },
    {
        path: "/faq",
        element: <DocPage Content={Faq} />,
    },
]);

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>
);
