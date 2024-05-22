## baseUrl: https://39xhlpq0-8000.asse.devtunnels.ms

## 1. Artist
    1.1 Lấy toàn bộ Artist
        Endpoint: {baseUrl}/artist/get-all-artists
        Method: GET
    1.2 Lấy Artist theo country
        Endpoint: {baseUrl}/artist/get-artists-by-country?country=Korea
        Method: GET
    1.3 Lấy All country
        Endpoint: {baseUrl}/artist/get-all-artist-country
        Method: GET
    1.4 Lấy popular artists
        Endpoint: {baseUrl}/artist/get-popular-artists?limit=3
        Method: GET
    1.5 Lấy artist theo id
        Endpoint: {baseUrl}/artist/get-artist-by-id?artist_id=
        Method: GET
## 2. Genres
    2.1 Lấy toàn bộ Genres
        Endpoint: {baseUrl}/genre/get-all-genres
        Method: GET
## 3. Tracks
    3.1 Lấy toàn bộ Track
        Endpoint: {baseUrl}/track/get-all-tracks
        method: GET
    3.2 Lấy track theo top trending
        Endpoint: {baseUrl}/track/get-top-trending-tracks?limit=5
        method: GET
    3.3 Lấy track theo Artist_id
        Endpoint: {baseUrl}/track/get-tracks-by-artist-id?artist_id=9DdPVHmCJEvSJrY9IxBV
        method: GET
    3.4 Lấy track theo genre_id
        Endpoint: {baseUrl}/track/get-tracks-by-genre-id?genre_id=H2B9zb6US83WMK1etKMJ
        method:GET
    3.5 Lấy shuffled-tracks
        Endpoint: {baseUrl}/track/get-shuffled-tracks?limit=5
        method: GET
    3.6 Lấy track theo id
        Endpoint: {baseUrl}/track/get-track-by-id?track_id=13Nmlsgxnumg3n2mljMh
        method: GET
    3.7 Lấy gợi ý tracks
        Endpoint: {baseUrl}/track/get-recommended-tracks?track_id=13Nmlsgxnumg3n2mljMh
        method: GET
    3.8 Lấy all tracks to search
        Endpoint: {baseUrl}/track/get-all-tracks-basic-info
        method: GET
## 4. Auth
    4.1 Đăng ký
        POST {baseUrl}/auth/signup 
        Content-Type: application/json
        { "email": "test2@mail.com", "password": "Pass1234!", "username": "Test2"  }

        Result:
            {"message": "successfully"}
            {"message": "failed", "error": "Email already exists"}
            {"message": "failed", "error": error_message}
    4.2 Login
        POST {baseUrl}/auth/login 
        Content-Type: application/json
        { "email": "test1@mail.com", "password": "Pass1234!" }

        Result:
           {"token": access_token}
           {"message": "Invalid credentials"}
           {"message": "User not found"}
    4.3 Check token
        GET {baseUrl}/auth/check-token 
        Content-Type: application/json 
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlRlc3QxIiwicm9sZSI6InVzZXIiLCJleHAiOjE3MTY3Nzg4NjV9.uk1AVWB1En5e5X267-pQBH0gHYFEaOgOvV81ZUQ413A
        {}

        Result:
            {"message": "Token is valid"}
            {"message": "Token expired"}
            {"message": "Invalid token"}
            {"message": "Authorization header missing"}
    4.5 Is-creator
        GET {baseUrl}/auth/is-creator
        Authorization: Bearer xxx
## 5. Playlists
    5.1 Create my playlist
        POST {baseUrl}/playlist/create-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "playlist_name":"relax" 
        }
    5.6 Remove my playlist
        POST {baseUrl}/playlist/remove-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "playlist_id": "hZTSUEYPgBLvZOWyV2sZ"
        }
    5.2 Get my playlists
        Method: POST 
        Endpoit: {baseUrl}/playlist/get-my-playlist
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI

    5.3 Get tracks by playlist_id
        Method: GET
        Endpoint: {baseUrl}/playlist/get-tracks-by-playlist-id?playlist_id=Skpez84xuwiWavLXXqPR
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
    5.4 Add track to playlist
        Method: POST
        Endpoint: {baseUrl}/playlist/add-track-to-my-playlist
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
        Endpont: {baseUrl}/playlist/remove-track-from-my-playlist
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
        Endpoint: {baseUrl}/playlist/get-tracks-recommend-by-playlist-id?playlist_id=Skpez84xuwiWavLXXqPR
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
    5.7 Change playlist_name
        Medtod: POST
        Endpoint: {baseUrl}/playlist/change-playlist-name
        Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZ1p3aUZRblZEVU53cjZmakxoUnV0ekZwSDc3MyIsInVzZXJuYW1lIjoiTGluaGxpbmgiLCJyb2xlIjoidXNlciIsImV4cCI6MTcxNjgxMjcyOX0.3HOlu6uAVe1YkeNoua1wQ2zfX0Isz3LM3Fz-QfkIbRI
        {
            "playlist_name": ""
            "playlist_id": ""
        }
## 6. Account
    6.1 change role
        Method: Post
        Endpoint: {baseUrl}/account/change-account-role
        Authorization: Bearer xxx
        {
            "new_role": ""
        }
    6.2 get information
        Method: Post
        Endpoint: {baseUrl}/account/get-account-information
        Authorization: Bearer xxx
        
        result:
            infor = {
                "user_id": user_id,
                "email": decoded_token["email"],
                "role": decoded_token["role"],
                "fullname": account_info["fullname"],
                "avatar_image": account_info["avatar_image"],
            }
    6.3 change fullname
        Method: Post
        Endpoint: {baseUrl}/account/update-fullname
        Authorization: Bearer xxx
        {
            "new_fullname": ""
        }
    6.4 change password
        Method: Post
        Endpoint: {baseUrl}/account/update-password
        Authorization: Bearer xxx
        {
            "new_password": "123456",
            "old_password": "Pass1234!"
        }
    6.4 Change avatar
        Method: Post
        Endpoint: {baseUrl}/account/update-avatar-image
        Authorization: Bearer xxx
        key: avatar_image
        FILE
