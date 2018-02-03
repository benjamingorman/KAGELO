from server.query import Query, Field, generic_create_or_update
import server.validators as validators

username = Field("username", validators.username)
nickname = Field("nickname", validators.nickname)
clantag  = Field("clantag", validators.clantag)
gender   = Field("gender", validators.gender, parser=int)
head     = Field("head", validators.head, parser=int)

region    = Field("region", validators.region)
kag_class = Field("kag_class", validators.kag_class)
rating    = Field("rating", validators.rating, parser=int)
score     = Field("score", validators.score, parser=int)
wins      = score.rename("wins")
losses    = score.rename("losses")

match_time = Field("match_time", validators.match_time, parser=int)

limit = Field("limit", validators.is_int)

player_row        = [username, nickname, clantag, gender, head]
player_rating_row = [username, region, kag_class, rating, wins, losses]
match_history_row = [region, username.rename("player1"), username.rename("player2"), kag_class, match_time,
                        score.rename("player1_score"), score.rename("player2_score"), score.rename("duel_to_score")]

get_player = Query(
    "SELECT * FROM players WHERE username=%s",
    [username],
    player_row
    )

create_or_update_player = Query(
    generic_create_or_update("players", ["username", "nickname", "clantag", "gender", "head"]),        
    [username, nickname.optional(), clantag.optional(), gender.optional(), head.optional()],
    []
    )

create_or_update_match_history = Query(
    generic_create_or_update("match_history", ["region", "player1", "player2", "kag_class", "match_time",
                                                            "player1_score", "player2_score", "duel_to_score"]),        
    [region, username.rename("player1"), username.rename("player2"), kag_class, match_time,
        score.rename("player1_score"), score.rename("player2_score"), score.rename("duel_to_score")],
    []
    )

get_player_rating = Query(
    "SELECT * FROM player_rating WHERE username=%s AND region=%s AND kag_class=%s",
    [username, region, kag_class],
    player_rating_row
    )

get_player_ratings = Query(
    "SELECT * FROM player_rating WHERE username=%s AND region=%s",
    [username, region],
    player_rating_row
    )

create_or_update_player_rating = Query(
    generic_create_or_update("player_rating", ["username", "region", "kag_class", "rating", "wins", "losses"]),
    [username, region, kag_class, rating.optional(), wins.optional(), losses.optional()],
    []
    )

get_match_history = Query(
    "SELECT * FROM match_history WHERE region=%s AND match_time=%s",
    [region, match_time],
    match_history_row
    )

get_player_match_history = Query(
    """
    SELECT * FROM match_history WHERE player1=%s OR player2=%s ORDER BY match_time DESC;
    """,
    [username, username],
    match_history_row
    )

get_recent_match_history = Query(
    "SELECT * FROM match_history ORDER BY match_time DESC LIMIT %s",
    [limit],
    match_history_row
    )

get_leaderboard = Query(
    """SELECT players.username, players.nickname, players.clantag, players.gender, players.head, player_rating.rating, player_rating.wins, player_rating.losses
FROM player_rating INNER JOIN players ON players.username=player_rating.username
WHERE player_rating.region=%s AND player_rating.kag_class=%s
ORDER BY player_rating.rating DESC;
    """,
    [region, kag_class],
    [username, nickname, clantag, gender, head, rating, wins, losses]
    )
