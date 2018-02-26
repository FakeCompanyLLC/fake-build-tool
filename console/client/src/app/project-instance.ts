export class ProjectInstance {
  _id: string;
  name: string;
  "version-override": string;
  remotes: any[];
  tag: string;
  commit: string;
  "revert-commit": string;
  "cherry-picks": any[];
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
