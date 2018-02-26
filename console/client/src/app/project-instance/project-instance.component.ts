import { Component, OnInit, Inject } from '@angular/core';
import { Project } from '../project';
import { ProjectName } from '../project-name';
import { ProjectInstance } from '../project-instance';
import { FbtService } from '../fbt.service';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-project-instance',
  templateUrl: './project-instance.component.html',
  styleUrls: ['./project-instance.component.css']
})
export class ProjectInstanceComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ProjectInstanceComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  cancel(): void {
    this.dialogRef.close();
  }

  ngOnInit() {

  }

  addModule(project) {
    if (!project.modules) {
      project.modules = [];
    }
    project.modules.push("");
  }

  addCommand(project) {
    if (!project.cmd) {
      project.cmd = [];
    }
    project.cmd.push("");
  }

  addProperty(project) {
    if (!project.properties) {
      project.properties = [];
    }
    project.properties.push("");
  }

  addRemote(project) {
    if (!project.remotes) {
      project.remotes = [];
    }
    project.remotes.push("");
  }

  addCherryPick(project) {
    if (!project['cherry-picks']) {
      project['cherry-picks'] = [];
    }
    project['cherry-picks'].push("");
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  removeCommand(commands: any, index: number) {
    commands.splice(index, 1);
  }

  removeProperty(properties: any, index: number) {
    properties.splice(index, 1);
  }

  removeModule(modules: any, index: number) {
    modules.splice(index, 1);
  }

  removeRemote(remotes: any, index: number) {
    remotes.splice(index, 1);
  }

  removeModule(cherryPicks: any, index: number) {
    cherryPicks.splice(index, 1);
  }

}
