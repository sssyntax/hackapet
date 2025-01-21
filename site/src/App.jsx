import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import Toolbar from "./components/Toolbar.jsx";
import "./App.css";
import EmailButton from "./components/EmailButton.jsx";

import { Outlet, Link } from "react-router-dom";

function App() {
    const [count, setCount] = useState(0);

    return (
        <>
            <div className="h-screen flex flex-col justify-center items-center">
                <img
                    src="/watercolorbg.png"
                    className="absolute top-0 w-full opacity-80"
                />
                <a
                    href="https://hackclub.com"
                    target="_blank"
                    rel="noopenner noreferrer"
                >
                    <img
                        src="https://assets.hackclub.com/flag-orpheus-top.svg"
                        className="absolute top-0 left-2"
                    />
                </a>
                <div className="absolute top-0 right-4">
                    <Toolbar />
                </div>
                <div className="flex flex-col justify-center items-center text-center text-[#FFFFFF] mb-20 z-10">
                    <img
                        src="/logo.svg"
                        className="w-full px-6 md:h-44 lg:h-64 xl:h-72"
                    />
                    <p className="mx-8 text-2xl text-darkPink md:mt-4 mt-8 retro">
                        Code a virtual pet. Get a tamagotchi clone!
                    </p>
                    {/*<button href="#" className="px-8 py-2 bg-slate mt-4 text-xl rounded-sm retro">coming VERY soon !!!</button>*/}
                    <EmailButton />
                    <img
                        src="/arrows.svg"
                        className="w-16 mt-16 lg:mt-8 bobble"
                    />
                </div>
                <img src="/herobg.png" className="absolute bottom-0 w-full" />
            </div>
            <div className="bg-darkBlue w-full py-10">
                <div className="flex flex-wrap justify-center gap-8 text-darkBlue retro mx-5">
                    <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
                        <p>1. draw and design your character + backgrounds!</p>
                    </div>
                    <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
                        <p>
                            2. code your game - make it playable on the device!
                        </p>
                    </div>
                    <div className="bg-lightBlue p-5 max-w-sm text-center rounded-sm">
                        <p>
                            3. submit your game + wait for the console to arrive
                            in mail!
                        </p>
                    </div>
                </div>
            </div>

            <div className="my-12">
                <div className="flex flex-col justify-center align-center">
                    <p className="text-center text-3xl retro text-darkBlue">
                        What's in the box?
                    </p>
                </div>

                <div className="flex flex-wrap justify-center items-center gap-8 mt-4">
                    <img src="tama1.png" className="w-96" />
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-black mx-5">
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">
                                Microcontroller - ESP32-S2FH4
                            </p>
                            <p className="text-lg neuebit">
                                Includes wifi capabilities!
                            </p>
                        </div>
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">Screen</p>
                            <p className="text-lg neuebit">
                                1.5in 128x128 pixels full color oled
                            </p>
                        </div>
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">Dimensions</p>
                            <p className="text-lg neuebit">
                                5.6x6.6cm - the size of an actual tamagotchi!
                            </p>
                        </div>
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">Extras!</p>
                            <p className="text-lg neuebit">
                                3 tactile buttons 3 LEDs for you to program
                            </p>
                        </div>
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">Hackable!</p>
                            <p className="text-lg neuebit">
                                16 pins broken out to add anything on
                            </p>
                        </div>
                        <div className="border-dashed border-4 border-darkBlue p-4">
                            <p className="text-sm text-darkBlue">
                                Battery - 2xAAA
                            </p>
                            <p className="text-lg neuebit">
                                Lasts around 8 hours*
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <div className="my-12 bg-darkBlue py-12">
                <div className="flex flex-col justify-center items-center text-center">
                    <p className="text-3xl text-lightBlue retro">
                        So... how can I get one?
                    </p>
                </div>
                <p className="text-lightBlue flex flex-col justify-center text-center mx-5 mt-4 neuebit-body">
                    Hackapet isn't for sale! As long as you're a teenager, create an original game and we'll personally mail you
                    one for free - "you ship, we ship!"
                </p>

                <div className="grid grid-cols-1 md:grid-cols-2 text-lightBlue text-xl mt-8 mx-5 xl:mx-44 gap-8">
                    <div className="">
                        <div className="border-4 border-dashed border-lightBlue p-8 text-sm">
                            <p className="text-2xl mb-4 neuebit-body">
                                How do I make a game?
                            </p>
                            <p className="neuebit">
                                For this, we'll be using{" "}
                                <a
                                    href="https://circuitpython.org/"
                                    className="link"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    CircuitPython
                                </a>
                                ! It's a programming language similar to Python,
                                used on microcontroller boards.
                            </p>
                            <p className="mt-4 neuebit">
                                You'll also need to use{" "}
                                <a
                                    href="https://pypi.org/project/blinka-displayio-pygamedisplay/"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    this library
                                </a>
                                , which allows you to output CircuitPython
                                displayio code to a pygame window on PC, instead
                                of a hardware display.
                            </p>
                            <p className="mt-4 neuebit">
                                To set that up, make a virtual enviorment by
                                using the commands below (for macOS and Linux
                                only!) (further instructions{" "}
                                <a
                                    href="https://pypi.org/project/blinka-displayio-pygamedisplay/"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    here
                                </a>
                                ):
                            </p>
                            <div className="bg-black bg-opacity-50 p-4 rounded-lg mt-4 code">
                                <p>mkdir project-name && cd project-name</p>
                                <p>python3 -m venv .env</p>
                                <p>source .env/bin/activate</p>
                                <p>
                                    pip3 install blinka-displayio-pygamedisplay
                                    adafruit-circuitpython-display-text
                                </p>
                            </div>
                            <p className="mt-4 neuebit">
                                For getting keyboard inputs, I use pygame. When
                                you get the actual device, you'll need to switch
                                out any pygame code for circuitpython.
                            </p>
                        </div>
                        <div className="border-4 border-dashed border-lightBlue p-8 mt-8 text-sm">
                            <p className="text-2xl mb-4 neuebit-body">
                                How do I draw pixel art?
                            </p>
                            <p className="neuebit">
                                I use{" "}
                                <a
                                    href="https://www.aseprite.org/"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    Aseprite
                                </a>
                                , a pixel art app! You can get it for free by
                                compiling it yourself{" "}
                                <a
                                    href="https://github.com/aseprite/aseprite/blob/main/INSTALL.md"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    here
                                </a>
                                .
                            </p>
                            <p className="mt-4 neuebit">
                                Don't want to compile anything? Download{" "}
                                <a
                                    href="https://libresprite.github.io/#!/"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    Libresprite
                                </a>
                                , an older version of Aesprite! Should work
                                similarily.
                            </p>
                            <p className="mt-4 neuebit">
                                Don't want to download anything?{" "}
                                <a
                                    href="https://www.piskelapp.com/"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    Piskel
                                </a>{" "}
                                is an online pixel art editor.
                            </p>
                            <p className="mt-4 neuebit">
                                Some asset suggestions:
                            </p>
                            <div className="ml-4 neuebit">
                                <p>
                                    ⁕ 2-3 different backgrounds! (128x128
                                    pixels)
                                </p>
                                <p>
                                    ⁕ character - idle/walking animations (rec
                                    32x32 to 64x64 pixels)
                                </p>
                                <p>⁕ food + other small items</p>
                            </div>

                            <p className="mt-4 neuebit">
                                After you're done drawing, download your files
                                as .bmp
                            </p>
                            <p className="mt-4 neuebit">
                                For animations, download the entire animation as
                                a singular sprite sheet file. You can cut it
                                into frames in code!
                            </p>
                            <img src="/cat-Sheet.png" className="w-full mt-4" />
                            <p className="opacity-70 mt-2 neuebit">
                                <i>
                                    Here's the sprite sheet for the idle
                                    animation of my pet!
                                </i>
                            </p>
                        </div>
                    </div>

                    <div className="border-4 border-dashed border-lightBlue p-8 text-sm neuebit-body">
                        <p className="text-2xl mb-4 neuebit">
                            How do I submit my game?
                        </p>
                        <p className="neuebit">Submission criteria:</p>
                        <div className="ml-4 neuebit">
                            <p>1. You must be in high school (or younger)</p>
                            <p>
                                2. The game must have at least 2 minutes of
                                gameplay
                            </p>
                            <p>3. It must be original</p>
                            <p>4. All art must be made by you</p>
                        </div>
                        <p className="mt-4 neuebit">How to submit:</p>
                        <div className="ml-4 neuebit">
                            <p>1. Fork the Hackapet repo on GitHub!</p>
                            <p>
                                2. Create a new folder in{" "}
                                <a
                                    href="https://github.com/hackclub/hackapet/tree/main/pets"
                                    target="_blank"
                                    rel="noopenner noreferrer"
                                >
                                    /pets
                                </a>{" "}
                                + put in your files (include art!)
                            </p>
                            <p>3. Make a pull request.</p>
                            <p>
                                4. If it gets merged, you're in! Wait for a form
                                to fill.
                            </p>
                        </div>
                        <a
                            href="https://github.com/hackclub/hackapet"
                            target="_blank"
                            rel="noopenner noreferrer"
                        >
                            <button className="p-4 bg-lightPink text-black rounded-sm mt-4 neuebit">
                                Submit your game by making a pull request!
                            </button>
                        </a>
                        <p className="mt-2 neuebit">
                            Questions? Ask in{" "}
                            <a
                                href="https://hackclub.slack.com/archives/C0809PN4TPE"
                                target="_blank"
                                rel="noopenner noreferrer"
                            >
                                #hackapet
                            </a>{" "}
                            in the Hack Club Slack!
                        </p>
                    </div>
                </div>
            </div>

            <div className="relative">
                <div className="px-12 mb-4 text-darkPink">
                    <p>Here are some pictures of the Hackapet prototype v2!</p>
                </div>

                <div className="px-12 flex flex-wrap pb-20">
                    <img
                        src="/pic1.png"
                        className="mr-8 mb-8 lg:mb-0 border-4 border-darkPink border-dashed"
                    />
                    <img
                        src="/pic2.png"
                        className="border-4 border-darkPink border-dashed"
                    />
                </div>

                <img src="/footerbg.png" className="w-full absolute bottom-0" />
            </div>

            <div className="bg-black w-full flex flex-col justify-center items-center text-lightBlue pt-4 md:pt-2 pb-6">
                <div className="text-center mx-5 neuebit leading-none">
                    <p>
                        site by @acon{" "}
                        <span className="opacity-70">
                            <i>
                                {" "}
                                - follow me on{" "}
                                <a
                                    href="https://github.com/acornitum"
                                    className="text-lightPink"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    github
                                </a>{" "}
                                for a special suprise!
                            </i>
                        </span>
                    </p>
                    <p>pcb by @acon, @dari // alexren, @cheru</p>
                    <p>
                        firmware by @dari // alexren
                        <span className="opacity-70">
                            <i>
                                {" "}
                                - follow me too ill send sticker {"->"}{" "}
                                <a
                                    href="https://github.com/qcoral"
                                    className="text-lightPink"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    github
                                </a>
                            </i>
                        </span>
                    </p>
                    <p>site art by @ItsKareem</p>
                </div>
            </div>
        </>
    );
}

export default App;
