import { Component, OnInit, Inject } from '@angular/core';
import { FbtService } from '../fbt.service';
import { Project } from '../project';
import { ProjectName } from '../project-name';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent implements OnInit {

  projects: Project[];

  constructor(
    private service: FbtService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    this.service.readProjects().subscribe((projects: Project[]) => {
      this.projects = projects;
    });
  }

  add() {
    this.openDialog();
  }

  openDialog(): void {
    let dialogRef = this.dialog.open(ProjectAddComponent, {
      width: '800px'
    });

    dialogRef.afterClosed().subscribe(name => {
      if (name) {
        let projectName = new ProjectName();
        projectName.name = name;
        this.service.createProject(projectName).subscribe((project: Project) => {
          this.projects.push(project);
        });
      }
    });
  }

}

@Component({
  selector: 'app-project-add',
  templateUrl: './project-add.component.html',
  styleUrls: ['./project-add.component.css']
})
export class ProjectAddComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<ProjectAddComponent>
  ) { }

  cancel(): void {
    this.dialogRef.close();
  }

  ngOnInit() {

  }

}
