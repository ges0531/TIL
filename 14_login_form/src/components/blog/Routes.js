import React from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';

import SignUp from "../sign/SignUp";
import SignInSide from "../sign/SignInSide";
import Blog from './Blog';

const Routes = () => {
    return (
      <HashRouter>
        <Switch>
          <Route path="/" component={Blog} exact={true} />
          <Route path="/SignUp" component={SignUp} />
          <Route path="/SignInSide" component={SignInSide} />
          {/* Not Found
          <Route component={() => <Redirect to="/" />} /> */}
        </Switch>
      </HashRouter>
    );
  };
  
  export default Routes;