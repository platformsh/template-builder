import React, { Component } from 'react';
import { HydraAdmin } from '@api-platform/admin';

let entrypoint = process.env.REACT_APP_PUBLIC_URL;
console.log("first ",entrypoint)

if(!entrypoint) { // default entrypoint to current url
    entrypoint = window.location.href;
}

class App extends Component {
    componentDidMount(){
        document.title = process.env.REACT_APP_ADMIN_SITE_NAME || "Admin API Platform.sh";
    }

    render() {
        return <HydraAdmin entrypoint={entrypoint}/>;
    }
}

export default App;
