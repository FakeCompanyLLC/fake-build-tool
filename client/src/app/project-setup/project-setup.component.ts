import { Component, OnInit, Inject } from '@angular/core';
import { Project } from '../project';
import { ProjectName } from '../project-name';
import { ProjectInstance } from '../project-instance';
import { FbtService } from '../fbt.service';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-project-setup',
  templateUrl: './project-setup.component.html',
  styleUrls: ['./project-setup.component.css']
})
export class ProjectSetupComponent implements OnInit {

  project: Project = new Project();

  constructor(
    private service: FbtService,
    private route: ActivatedRoute,
    private router: Router,
    public dialog: MatDialog
  ) {
    this.project.name = new ProjectName();
  }

  ngOnInit() {
    let id = this.route.snapshot.paramMap.get('id');
    if (id && id != 'new') {
      this.service.readProject(id).subscribe(project => {
        console.log(this.project);
        this.project = project;
      })
    }
  }

  new() {
    this.openDialog(new ProjectInstance());
  }

  edit(instance: ProjectInstance): void {
    this.openDialog(instance);
  }

  save(instance: ProjectInstance) {
    if (instance._id) {
      this.service.updateProjectInstance(instance._id, instance).subscribe();
    } else {
      console.log(this.project._id);
      this.service.createProjectInstance(this.project._id, instance).subscribe((instance: ProjectInstance) => {
        this.project.instances.push(instance);
      });
    }
  }

  openDialog(instance: ProjectInstance): void {
    let dialogRef = this.dialog.open(ProjectInstanceComponent, {
      width: '800px',
      data: {instance: instance}
    });

    dialogRef.afterClosed().subscribe(instance => {
      this.save(instance);
    });
  }

}

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

}
