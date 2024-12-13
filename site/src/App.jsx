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
        <div className="flex flex-col justify-center items-center text-center text-[#FFFFFF] mb-24">
          <img src="/logo.svg" className="w-full px-6 md:h-44 lg:h-64 xl:h-72" />
          <p className="mx-5 text-xl text-darkPink mt-4">Code a virtual pet. Get a tamagotchi clone!</p>
          <button href="#" className="px-8 py-2 bg-lightPink mt-2 text-xl rounded-sm">join now !!!!!!</button>
        </div>
        <img src="/herobg.png" className="absolute bottom-0 w-full"/>
      </div>
      <div className="bg-darkBlue w-full py-10">
        <div className="flex flex-wrap justify-center gap-8">
          <div className="bg-lightBlue p-5 max-w-sm text-center">
            <p>1. draw and design your character + backgrounds!</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm text-center">
            <p>2. program your game - make it move, etc</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm text-center">
            <p>3. submit your game - then wait for your package to arrive in the mail!</p>
          </div>
        </div>
      </div>
      <h>fdjsk</h>
    </>
  );
}

export default App;
