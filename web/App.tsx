import React, {useState} from 'react';
import {Dialog} from "@headlessui/react";

function App() {
    const [isOpen,setIsOpen] = useState(true)
    // @ts-ignore
    window.onDevKitClick = () => {
        setIsOpen(true)
    }
    return (

        <Dialog onClose={setIsOpen} open={isOpen}>
            <div className="fixed inset-0 flex items-center justify-center p-2  z-50 w-screen">
                <div className={"bg-comfy-light rounded-3xl"}>
                    <div className="flex flex-col items-center justify-center p-4">
                        <h1 className="text-2xl font-bold">Comfy Dev Kit</h1>
                        <p className="text-sm">Work in progress</p>
                    </div>
                    <div className="flex flex-col space-y-2 items-center justify-center p-4">
                        <button onClick={() => fetch('/devkit/reload').then(()=>setIsOpen(false))} className="bg-comfy-dark text-white border-0 px-4 py-2 rounded-md cursor-pointer">Refresh Nodes</button>
                        <button onClick={() => setIsOpen(false)} className="bg-comfy-dark text-white border-0 px-4 py-2 rounded-md cursor-pointer">Close</button>
                    </div>
                </div>

            </div>

        </Dialog>
);
}

export default App;