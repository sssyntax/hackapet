import React from "react";
import { Link } from "react-router-dom";

const DocPage = ({ Content }) => {
  return (
    <div className="">
      <header className="p-4 border-darkBlue border-b-4 bg-darkBlue">
          <Link to="/" className="text-lightBlue hover:text-lightPink no-underline bg-darkBlue p-2 px-6 rounded-lg text-lg">
            {"<<"} back to Hackapet homepage
          </Link>
      </header>
      <div className="flex">
        <aside className="p-5 border-dashed border-r-4 border-darkBlue">
        <nav className="flex flex-col space-y-2 hover:bg-lightPink p-2 rounded-lg px-4">
            <Link to="/setup" className="text-darkBlue hover:text-darkPink no-underline">
              Setup
            </Link>
          </nav>
          <nav className="flex flex-col space-y-2 hover:bg-lightPink p-2 rounded-lg px-4">
            <Link to="/art" className="text-darkBlue hover:text-darkPink no-underline">
              Art
            </Link>
          </nav>
          <nav className="flex flex-col space-y-2 hover:bg-lightPink p-2 rounded-lg px-4">
            <Link to="/guide" className="text-darkBlue hover:text-darkPink no-underline">
              Guide
            </Link>
          </nav>
          <nav className="flex flex-col space-y-2 hover:bg-lightPink p-2 rounded-lg px-4">
            <Link to="/submitting" className="text-darkBlue hover:text-darkPink no-underline">
              Submitting
            </Link>
          </nav>
          <nav className="flex flex-col space-y-2 hover:bg-lightPink p-2 rounded-lg px-4">
            <Link to="/FAQ" className="text-darkBlue hover:text-darkPink no-underline">
              FAQ
            </Link>
          </nav>
        </aside>

        <div className="flex flex-col w-full m-14">
          <main className="prose w-full poppins">
            <Content />
          </main>
        </div>

      </div>
    </div>
  );
};

export default DocPage;