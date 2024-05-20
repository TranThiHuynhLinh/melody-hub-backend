## 1. Artist
    1.1 Lấy toàn bộ Artist
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/artist/get-all-artists
        Method: GET
    1.2 Lấy Artist theo country
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/artist/get-artists-by-country?country=Korea
        Method: GET
    1.3 Lấy All country
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/artist/get-all-artist-country
        Method: GET
    1.4 Lấy popular artists
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/artist/get-popular-artists?limit=3
        Method: GET
## 2. Genres
    2.1 Lấy toàn bộ Genres
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/genre/get-all-genres
        Method: GET
## 3. Tracks
    3.1 Lấy toàn bộ Track
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/track/get-all-tracks
        method: GET
    3.2 Lấy track theo top trending
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/track/get-top-trending-tracks?limit=5
        method: GET
    3.3 Lấy track theo Artist_id
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/track/get-tracks-by-artist-id?artist_id=9DdPVHmCJEvSJrY9IxBV
        method: GET
    3.4 Lấy track theo genre_id
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/track/get-tracks-by-genre-id?genre_id=H2B9zb6US83WMK1etKMJ
        method:GET
    3.5 Lấy shuffled-tracks
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/track/get-shuffled-tracks?limit=5
        method: GET
## 4. Auth
    4.1 Đăng ký
        POST https://39xhlpq0-8000.asse.devtunnels.ms/auth/signup 
        Content-Type: application/json
        { "email": "test2@mail.com", "password": "Pass1234!", "username": "Test2"  }

        Result:
            {"message": "successfully"}
            {"message": "failed", "error": "Email already exists"}
            {"message": "failed", "error": error_message}
    4.2 Login
        POST https://39xhlpq0-8000.asse.devtunnels.ms/auth/login 
        Content-Type: application/json
        { "email": "test1@mail.com", "password": "Pass1234!" }

        Result:
           {"token": access_token}
           {"message": "Invalid credentials"}
           {"message": "User not found"}
    4.3 Check token
        GET https://39xhlpq0-8000.asse.devtunnels.ms/auth/check-token 
        Content-Type: application/json 
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRlc3QxIiwicm9sZSI6InVzZXIiLCJleHAiOjE3MTY3Nzg4NjV9.uk1AVWB1En5e5X267-pQBH0gHYFEaOgOvV81ZUQ413A
        {}

        Result:
            {"message": "Token is valid"}
            {"message": "Token expired"}
            {"message": "Invalid token"}
            {"message": "Authorization header missing"}
## 5. Playlists
    5.1 Create my playlist
        POST https://39xhlpq0-8000.asse.devtunnels.ms/playlist/create-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "playlist_name":"relax" 
        }
    5.6 Remove my playlist
        POST https://39xhlpq0-8000.asse.devtunnels.ms/playlist/remove-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "playlist_id": "hZTSUEYPgBLvZOWyV2sZ"
        }
    5.2 Get my playlists
        Method: POST 
        Endpoit: https://39xhlpq0-8000.asse.devtunnels.ms/playlist/get-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI

    5.3 Get tracks by playlist_id
        Method: GET
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/playlist/get-tracks-by-playlist-id?playlist_id=Skpez84xuwiWavLXXqPR
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
    5.4 Add track to playlist
        Method: POST
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/playlist/add-track-to-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "track_id": "oAlB0uGlPWO3EsBB9yqu",
            "playlist_id": "hZTSUEYPgBLvZOWyV2sZ"
        }
        result:
            {"message": "successfully"}
            {"message": "Track already exists in playlist"}
    5.5 Remove track from playlist
        Method: POST
        Endpont: https://39xhlpq0-8000.asse.devtunnels.ms/playlist/remove-track-from-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "track_id": "oAlB0uGlPWO3EsBB9yqu",
            "playlist_id": "hZTSUEYPgBLvZOWyV2sZ"
        }
        result:
            {"message": "successfully"}
            {"message": "Playlist not found"}
            {"message": "Track does not exist in playlist"}
    5.6 Get track_recommended_by_playlist_id
        Medtod: GET
        Endpoint: https://39xhlpq0-8000.asse.devtunnels.ms/playlist/get-tracks-recommend-by-playlist-id?playlist_id=Skpez84xuwiWavLXXqPR
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI