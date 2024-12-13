import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="h-screen flex flex-col justify-center items-center">
        <img src="https://assets.hackclub.com/flag-orpheus-top.svg" className="absolute top-0 left-2"/>
        <div className="flex flex-col justify-center items-center text-center">
          <img src="/logo.svg" className="w-full px-6 md:h-44 lg:h-64 xl:h-72" />
          <p>Code a virtual pet. Get a tamagotchi clone!</p>
        </div>
        <img src="/herobg.png" className="absolute bottom-0 w-full"/>
      </div>
      <div className="bg-darkBlue w-full py-10">
        <div className="flex flex-wrap justify-center gap-8">
          <div className="bg-lightBlue p-5 max-w-sm">
            <p>1. draw and design your character + backgrounds!</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm">
            <p>2. program your game - make it move, etc</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm">
            <p>3. submit your game - and wait for your package in the mail!</p>
          </div>
        </div>
      </div>
      <h>fdjsk</h>
    </>
  );
}

export default App;
