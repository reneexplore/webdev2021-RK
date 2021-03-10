import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Album } from '../album/models';
import {Location} from '@angular/common';
import { AlbumsService } from '../albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit {
  album: Album;
  constructor(
    private route: ActivatedRoute,
    private location:Location,
    private albumsService: AlbumsService
  ) { }

  ngOnInit(): void {
    //const id = +this.route.snapshot.paramMap.get('id');
    //this.album = ALBUMS.find((x) => x.id === id);
    this.getAlbum();

  }
  getAlbum(){
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.albumsService.getAlbum(id).subscribe((album) => {
        this.album = album;
      });
      });
  }
  updateAlbum(){
    this.albumsService.updateAlbum(this.album).subscribe((album) => {
      console.log(album);
    })
  }
  goBack(){
    this.location.back();
  }

}
