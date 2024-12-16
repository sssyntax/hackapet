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
          <p className="mx-8 text-2xl text-darkPink md:mt-4 mt-8 retro">Code a virtual pet. Get a tamagotchi clone!</p>
          <button href="#" className="px-8 py-2 bg-lightPink mt-4 text-xl rounded-sm retro">join now !!!!!!</button>
        </div>
        <img src="/herobg.png" className="absolute bottom-0 w-full"/>
      </div>
      <div className="bg-darkBlue w-full py-10">
        <div className="flex flex-wrap justify-center gap-8 text-darkBlue retro">
          <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
            <p>1. draw and design your character + backgrounds!</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
            <p>2. code your game - make it playable on the device!</p>
          </div>
          <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
            <p>3. submit your game and wait for a package to arrive in the mail!</p>
          </div>
        </div>
      </div>

      <div className="my-12">
        <div className="flex flex-col justify-center align-center">
          <p className="text-center text-3xl retro text-darkBlue">What's in the box?</p>
        </div>
        <p></p>
      </div>
      
      <img src="/footerbg.png" className="w-full"/>
      <div className="bg-black w-full flex flex-col justify-center items-center text-lightBlue pt-4 md:pt-2 pb-6">
        <div className="text-center mx-5">
          <p>made by @acon <span className="opacity-70"><i> - follow me on <a href="https://github.com/acornitum" className="text-lightPink" target="_blank" rel="noopener noreferrer">github</a> for a special suprise!</i></span></p>
          <p>site art by @ItsKareem</p>
        </div>
      </div>
    </>
  );
}

export default App;
