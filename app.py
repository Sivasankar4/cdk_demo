#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_new.cdk_new_stack import CdkNewStack


app = cdk.App()
CdkNewStack(app, "CdkNewStack")

app.synth()
