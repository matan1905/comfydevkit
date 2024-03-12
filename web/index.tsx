import * as React from 'react';

import * as ReactDOM from "react-dom/client";
import App from "./App";

const rootDomNode = document.createElement('div');
document.body.appendChild(rootDomNode);
const root = ReactDOM.createRoot(rootDomNode);
root.render(<App />);

