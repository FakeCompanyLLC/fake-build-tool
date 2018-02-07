import { Component, OnInit, AfterViewChecked, ElementRef, ViewChild } from '@angular/core';
import { FbtService } from '../fbt.service';
import { MatSnackBar } from '@angular/material';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Profile } from '../profile';

@Component({
  selector: 'app-profile-status',
  templateUrl: './profile-status.component.html',
  styleUrls: ['./profile-status.component.css']
})
export class ProfileStatusComponent implements OnInit, AfterViewChecked {
  @ViewChild('scroller') private scroller: ElementRef;

  isLoading = false;
  isRunning = false;
  message = 'None';
  progress = 0;
  status = '';
  elapsed = '';
  line = '';
  maxLength = 50000;
  profile: Profile;

  constructor(
    private service: FbtService,
    private snackBar: MatSnackBar,
    private route: ActivatedRoute,
  ) { }

  ngAfterViewChecked() {
    if (this.scroller) {
      this.scrollToBottom();
    }
  }

  scrollToBottom(): void {
    let scrollPosition = this.scroller.nativeElement.scrollTop + this.scroller.nativeElement.offsetHeight;
    let scrollTotal = this.scroller.nativeElement.scrollHeight;

    try {
      if (scrollPosition >= scrollTotal - this.scroller.nativeElement.offsetHeight) {
        this.scroller.nativeElement.scrollTop = this.scroller.nativeElement.scrollHeight;
      }
    } catch(err) { }
  }

  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    if (id && id != 'new') {
      this.service.readProfile(id).subscribe((profile: Profile) => {
        this.profile = profile;
      })
    }

    let self = this;
    this.service.listen('message').subscribe(data => {
      self.isLoading = false;
      self.isRunning = true;
      let status = JSON.parse(data);
      if (status.elapsed_time) {
        self.elapsed = status.elapsed_time;
      }
      if (status.progress) {
        self.progress = status.progress * 100;
      }
      if (status.statusText) {
        self.status = status.statusText;
      }
      if (status.lines) {
        if (self.line.length > self.maxLength) {
          self.line = self.line.substring(self.line.length - self.maxLength, self.line.length);
        }
        self.line += status.lines;
      }
    });
  }

  stop() {
    this.isLoading = false;
    let self = this;
    this.service.stop().subscribe(() => {
      self.isRunning = false;
    });
  }

  start() {
    // this.isLoading = true;
    this.line = "";
    this.service.run(this.profile).subscribe();
    this.openSnackBar()
  }

  openSnackBar() {
    this.snackBar.openFromComponent(StartBuildComponent, {
      duration: 2000,
    });
  }
}

@Component({
  selector: 'starting-build',
  template: 'Starting Build',
})
export class StartBuildComponent {}
