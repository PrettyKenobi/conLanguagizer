import React from 'react';
import { Switch, Route } from 'react-router-dom';
import routes from './constants/routes.json';
import App from './containers/App';
import HomePage from './containers/HomePage';
import LexiconPage from './containers/LexiconPage';

export default function Routes() {
  return (
    <App>
      <Switch>
        <Route path={routes.LEXICON} component={LexiconPage} />
        <Route path={routes.HOME} component={HomePage} />
      </Switch>
    </App>
  );
}
