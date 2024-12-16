import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div className="h-screen flex flex-col justify-center items-center">
        <img src="/watercolorbg.png" className="absolute top-0 w-full opacity-80"/>
        <a href="https://hackclub.com" target="_blank" rel="noopenner noreferrer"><img src="https://assets.hackclub.com/flag-orpheus-top.svg" className="absolute top-0 left-2"/></a>
        <div className="flex flex-col justify-center items-center text-center text-[#FFFFFF] mb-20 z-10">
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

        <div className="flex flex-wrap justify-center items-center gap-8 mt-4">
          <img src="tama1.png" className="w-96"/>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-black mx-5">
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">Microcontroller - ESP32 S2 mini 2</p>
              <p className="text-lg">Includes wifi + bluetooth capabilities!</p>
            </div>
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">Screen</p>
              <p className="text-lg">1.5in 128x128 pixels full color oled</p>
            </div>
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">PCB Dimentions - 5.6x6.6cm</p>
              <p className="text-lg">The size of an actual tamagotchi!</p>
            </div>
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">Additional parts</p>
              <p className="text-lg">3 buttons and 3 LEDs for you to program</p>
            </div>
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">Hackable!</p>
              <p className="text-lg">16 pins broken out to add anything on</p>
            </div>
            <div className="border-dashed border-4 border-darkBlue p-4">
              <p className="text-sm text-darkBlue">Battery - 2xAAA</p>
              <p className="text-lg">Lasts around 8 hours*</p>
            </div>
          </div>
        </div>
      </div>

      <div className="my-12 bg-darkBlue py-12">
        <div className="flex flex-col justify-center items-center text-center">
          <p className="text-3xl text-lightBlue retro">So... how can I get one?</p>
        </div>

        <div className="mx-44 text-lightBlue text-xl mt-4">
          <p>Hackapet isn't for sale! Build an original game and we'll personally mail you one - "you ship, we ship!"</p>

          <p>How do I make a game?</p>
          <p>Circuitpython! We'll be using [this] so that you can display circuitpython on your PC, without the hardware.</p>
        
        <button className="p-4 bg-lightPink text-black rounded-sm mt-8">Submit your game by making a pull request!</button>
        </div>


      </div>

      <div className="">
        <img src="/footerbg.png" className="w-full"/>
      </div>
      


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
