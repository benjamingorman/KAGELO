import React, { Component } from 'react';
//import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { Switch, Route } from 'react-router-dom';
import 'react-tabs/style/react-tabs.css';
import './App.css';
import MainNavBar from './components/MainNavBar';
import MainFooter from './components/MainFooter';
import LeaderboardPage from './pages/LeaderboardPage';
import RecentMatchHistoryPage from './pages/RecentMatchHistoryPage';
import PlayerProfilePage from './pages/PlayerProfilePage';
import MatchPage from './pages/MatchPage';
import ClansPage from './pages/ClansPage';
import ClanPage from './pages/ClanPage';
import AboutPage from './pages/AboutPage';

class App extends Component {

    render() {
        return (
            <div className="App">
                <MainNavBar />

                <Switch>
                    <Route path='/player/:username' component={PlayerProfilePage} />
                    <Route path='/match/:matchID' component={MatchPage} />
                    <Route path='/recent_match_history' component={RecentMatchHistoryPage} />
                    <Route path='/clans' component={ClansPage} />
                    <Route path='/clan/:clantag' component={ClanPage} />
                    <Route path='/about' component={AboutPage} />
                    <Route path='/' component={LeaderboardPage} />
                </Switch>

                <MainFooter />
            </div>
        );
    }
}
/*
<Tabs defaultIndex={0}>
    <TabList>
        <Tab>Leaderboard</Tab>
        <Tab>Match History</Tab>
            <Tab>Player Profiles</Tab>
        </TabList>

        <TabPanel>
        </TabPanel>

        <TabPanel>
            <MatchHistory />
        </TabPanel>

        <TabPanel>
            <PlayerProfile username="Eluded" />
        </TabPanel>
    </Tabs>
*/

export default App;
