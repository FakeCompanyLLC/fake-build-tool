export class ProjectInstance {
  _id: string;
  name: string;
  "version-override": string;
  modules: any[];
  cmd: any[];
  properties: any[];
  profile: string;
  auth: boolean;
  "replace-subfloor": boolean;
  branch: string;
  "copy-overrides": boolean;
  fork: string;
  deploy: boolean;
}
