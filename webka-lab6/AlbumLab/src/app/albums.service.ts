import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import { HttpClient } from '@angular/common/http';
import {Album, Photo} from './album/models';


@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  BASE_URL = 'https://jsonplaceholder.typicode.com';

  constructor(private client: HttpClient) { }

  getAlbums(): Observable<Album[]>{
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`);
  }

  getAlbum(id: number): Observable<Album>{
    //const album = ALBUMS.find((x) => x.id === id);
    //return of (album);
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`);
  }
  updateAlbum(album: Album): Observable<Album>{
    return this.client.put<Album>(`${this.BASE_URL}/albums/${album.id}`, album);

  }
  addAlbum(album: Album): Observable<Album>{
    return this.client.post<Album>(`${this.BASE_URL}/albums`, album);

  }
  deleteAlbum(id: number): Observable<any>{

    return this.client.delete(`${this.BASE_URL}/albums/${id}`);
  }
  showPhotos(id: number): Observable<Photo[]> {
    return this.client.get<Photo[]>(`${this.BASE_URL}/albums/${id}/photos`);
  }
}
