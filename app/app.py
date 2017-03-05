import falcon
import json

from app.middleware import SessionWrapper, JSendTranslator
from resources import (
    ProtocolsResource,
    ProtocolResource,
    ProtocolPublicListResource,
    ProtocolVersionsResource,
    ProtocolVersionResource,
    OrganizationsResource,
    OrganizationResource,
    OrganizationGroupsResource,
    OrganizationGroupResource,
    OrganizationGroupMembersResource,
    OrganizationGroupMemberResource,
    OrganizationMdsLinksResource,
    OrganizationMdsLinkResource,
)

app = falcon.API(
    middleware=[
        SessionWrapper(),
        JSendTranslator(),
    ]
)

# Users
# ...


# Protocols
protocol = ProtocolResource()
protocols = ProtocolsResource()
public_protocols = PublicProtocolsResource()

app.add_route('/protocols/', protocols)
app.add_route('/protocols/public', public_protocols)
app.add_route('/protocols/{protocol_id}', protocol)
app.add_route('/organizations/{organization_id}/protocols/', protocols)
app.add_route('/organizations/{organization_id}/protocols/{protocol_id}', protocol)


# Protocol Versions
protocol_versions = ProtocolVersionsResource()
protocol_version = ProtocolVersionResource()

app.add_route('/protocols/{protocol_id}/versions/', protocol_versions)
app.add_route('/protocols/{protocol_id}/versions/{version_id}', protocol_version)


# Organizations
organizations = OrganizationsResource()
organization = OrganizationResource()

app.add_route('/organizations/', organizations)
app.add_route('/organizations/{organization_id}', organization)


# Organization Members
organization_members = OrganizationMembersResource()
organization_member = OrganizationMemberResource()

app.add_route('/organizations/', organization_members)
app.add_route('/organizations/{organization_id}', organization_member)


# Organization Groups
organization_group = OrganizationGroupResource()
organization_groups = OrganizationGroupsResource()

app.add_route('/organizations/{organization_id}/groups', organization_groups)
app.add_route('/organizations/{organization_id}/groups/{group_id}', organization_group)


# Organization Group Members
organization_group_member = OrganizationGroupMemberResource()
organization_group_members = OrganizationGroupMembersResource()

app.add_route(
    '/organizations/{organization_id}/groups/{group_id}/members',
    organization_group_members
)
app.add_route(
    '/organizations/{organization_id}/groups/{group_id}/members/{member_id}',
    organization_group_member
)


# Organization MDS Links
organization_mds_link = OrganizationMdsLinkResource()
organization_mds_links = OrganizationMdsLinksResource()

app.add_route(
    '/organizations/{organization_id}/mds_links/',
    organization_mds_links
)
app.add_route(
    '/organizations/{organization_id}/mds_links/{mds_link_id}',
    organization_mds_link
)


# Organization MDS Link Protocols
organization_mds_link_protocols = OrganizationMdsLinkProtocolsResource()
organization_mds_link_protocol = OrganizationMdsLinkProtocolResource()
organization_mds_link_synchronize = OrganizationMdsLinkSynchronizeResource()

app.add_route(
    '/organizations/{organization_id}/mds_links/{mds_link_id}/protocols/',
    organization_mds_link_protocols
)
app.add_route(
    '/organizations/{organization_id}/mds_links/{mds_link_id}/protocols/{protocol_id}',
    organization_mds_link_protocol
)
app.add_route(
    '/organizations/{organization_id}/mds_links/{mds_link_id}/synchronize',
    organization_mds_link_synchronize
)
