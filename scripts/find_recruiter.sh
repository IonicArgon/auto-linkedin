python3 -m src.recruiter find \
--url 'https://www.linkedin.com/talent/search/api/talentRecruiterSearchHits?decoration=%28entityUrn%2ClinkedInMemberProfileUrn~%28entityUrn%2CreferenceUrn%2Canonymized%2CunobfuscatedFirstName%2CunobfuscatedLastName%2CmemberPreferences%28openToNewOpportunities%2CproxyPhoneNumberAvailability%29%2CcanSendInMail%2CcontactInfo%28primaryEmail%29%2CcurrentPositions*%28company~%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%2Cdescription%2Clocation%29%2Ceducations*%28school~%28entityUrn%2Cname%29%2CorganizationUrn~%2CschoolName%2CdegreeName%2CstartDateOn%2CendDateOn%29%2CfirstName%2CfullProfileNotVisible%2CfullProfileNotVisibleReason%2Cheadline%2CindustryName%2ClastName%2Clocation%28displayName%29%2CnetworkDistance%2CnumConnections%2CprivacySettings%28allowConnectionsBrowse%2CshowPremiumSubscriberIcon%29%2CprofilePicture%2CpublicProfileUrl%2Cunlinked%2CvectorProfilePicture%2CworkExperience*%28company~%28entityUrn%2Cindustries%2Cname%29%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%29%29%2CrecruitingProfile~%28entityUrn%2Ccandidate%2CcurrentHiringProjectCandidate%28created%2ClastModified%2CentityUrn%2ChiringProject~%28entityUrn%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2Cnotes*%28candidate%2CchildNotes*%28candidate%2CchildNotes*%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2CprofileUrl%2Cprospect%2Ctags*%29%2ChiringProjectRecruitingProfile~%3AhiringProjectRecruitingProfile%28entityUrn%2CassessedCandidate%28rejectable%29%2Ccandidate%2CcurrentHiringProjectCandidate%28entityUrn%2Ccreated%2ClastModified%2CaddedToPipeline%28time%2Cactor~%28profile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%29%2ChiringProject~%28entityUrn%2ChiringProjectMetadata%28hiringPipelineEnabled%2Cstate%29%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2ClastActivity~%28activityType%2Cperformed%28time%2Cactor~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2CperformedByViewer%2ChiringActivityData%29%2CsourcingChannel%2CsourcingChannelCandidates*%2CassessmentCandidateQualificationResponses*%28assessmentQualificationUrn%2CrecruiterReplyDueAt%2CresponseSubmittedAt%29%2CcandidateInsights%28candidateHiringProjectInsightsUrn~%28candidateSimilarity%2CentityUrn%29%29%2C~hiringProjectCandidatesCount%28paging%29%29%2CcandidateInsights%28candidateSearchInsightsUrn~%28positionsInsight%2CyearsOfExperience%2CentityUrn%29%29%29&count=25&q=recruiterSearch&query=(capSearchSortBy:RELEVANCE,facets:List(TALENT_POOL))&requestParams=(searchContextId:a84b1345-28c2-4233-bc44-41be03989667,searchRequestId:3db1e7f3-d06f-48a0-9440-2aca4cbefb2b,searchHistoryId:10187933914,doFacetCounting:true,doFacetDecoration:true,uiOrigin:FACET_SEARCH,reset:List(),resetProfileCustomFields:List())&start=0' \
--identity ../identities/appleseed \
--output ../data/recruiter/leads/desautels_2025_2026.json \
--start 0 \
--count 25 \
--end 400